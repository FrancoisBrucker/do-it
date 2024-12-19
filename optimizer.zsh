#!/bin/zsh

if [[ "$1" == "--rewrite-git-history" ]]; then
    REWRITE_GIT_HISTORY=true
    shift
fi

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: optimizer.zsh <image|video|audio>"
    echo "Optimize media files in the current directory."
    exit 0
fi

temp_file=$(mktemp) # Temporary file to store paths for git filter-repo

if [[ "$1" == "image" || "$2" == "image" || "$3" == "image" ]]; then
    # Process image files (JPG, JPEG, PNG)
    find src -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.JPG" -o -name "*.JPEG" -o -name "*.PNG" \) -print0 | while IFS= read -r -d '' img; do
        ffmpeg -y -i "$img" -q:v 75 "${img%.*}.webp" && \
        echo "$img" >> "$temp_file" && \
        rm "$img"

        if [[ "$REWRITE_GIT_HISTORY" == "true" ]]; then
             git rm --cached "$img"
        fi
    done

    # Update image references in HTML files
    find src -type f -name "*.md" -exec sed -i \
        -e '/http/! s/\.png/\.webp/g' \
        -e '/http/! s/\.PNG/\.webp/g' \
        -e '/http/! s/\.jpg/\.webp/g' \
        -e '/http/! s/\.JPG/\.webp/g' \
        -e '/http/! s/\.jpeg/\.webp/g' \
        -e '/http/! s/\.JPEG/\.webp/g' {} +

elif [[ "$1" == "video" || "$2" == "video" || "$3" == "video" ]]; then
    # Process video files (MP4, MOV, MKV)
    find src -type f \( -name "*.mp4" -o -name "*.mov" -o -name "*.mkv" \) -print0 | while IFS= read -r -d '' video; do
        ffmpeg -y -i "$video" -c:v libx264 -preset veryslow -c:a aac -b:a 96k "${video%.*}.compressed.mp4" && \
        echo "$video" >> "$temp_file" && \
        rm "$video" && \
        mv "${video%.*}.compressed.mp4" "${video%.*}.mp4"

        if [[ "$REWRITE_GIT_HISTORY" == "true" ]]; then
             git rm --cached "$video"
        fi
    done

    # Update video references in HTML files
    find src -type f -name "*.md" -exec sed -i \
        -e '/http/! s/\.mp4/\.compressed\.mp4/g' \
        -e '/http/! s/\.mov/\.compressed\.mp4/g' \
        -e '/http/! s/\.mkv/\.compressed\.mp4/g' {} +


elif [[ "$1" == "audio" || "$2" == "audio" || "$3" == "audio" ]]; then
    # Process audio files (WAV, FLAC, MP3, OGG)
    find src -type f \( -name "*.wav" -o -name "*.flac" -o -name "*.mp3" -o -name "*.ogg" \) -print0 | while IFS= read -r -d '' audio; do
        ffmpeg -y -i "$audio" -c:a libopus -b:a 96k "${audio%.*}.opus" && \
        echo "$audio" >> "$temp_file" && \
        rm "$audio"

        if [[ "$REWRITE_GIT_HISTORY" == "true" ]]; then
             git rm --cached "$audio"
        fi
    done

    # Update audio references in HTML files
    find src -type f -name "*.md" -exec sed -i \
        -e '/http/! s/\.wav/\.opus/g' \
        -e '/http/! s/\.flac/\.opus/g' \
        -e '/http/! s/\.mp3/\.opus/g' \
        -e '/http/! s/\.ogg/\.opus/g' {} +

else
    echo "Usage: optimizer.zsh <image|video|audio>"
    exit 1
fi

# Rewrite git history for all stored paths
if [[ -s "$temp_file" && "$REWRITE_GIT_HISTORY" == "true" ]]; then
    git filter-repo --invert-paths --paths-from-file "$temp_file" --force
fi

# Cleanup temporary file
rm "$temp_file"
