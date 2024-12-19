#!/bin/zsh

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: optimizer.zsh <image|video|audio>"
    echo "Optimize media files in the current directory."
    exit 0
fi

temp_file=$(mktemp) # Temporary file to store paths for git filter-repo

if [[ "$1" == "image" ||  "$2" == "image" || "$3" == "image" ]]; then
    # Process image files (JPG, JPEG, PNG)
    find ./src -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read -r img; do
        img_clean="${img#./}" # Remove './' prefix
        ffmpeg -i "$img" -q:v 75 "${img_clean%.*}.webp" && \
        git rm --cached "$img_clean" && \
        echo "$img_clean" >> "$temp_file" && \
        rm "$img_clean"
    done

elif [[ "$1" == "video" ||  "$2" == "video" || "$3" == "video" ]]; then
    # Process video files (MP4, MOV, MKV)
    find ./src -name "*.mp4" -o -name "*.mov" -o -name "*.mkv" | while read -r video; do
        video_clean="${video#./}" # Remove './' prefix
        ffmpeg -y -i "$video" -c:v libx264 -preset veryslow -c:a aac -b:a 96k "${video_clean%.*}.compressed.mp4" && \
        git rm --cached "$video_clean" && \
        echo "$video_clean" >> "$temp_file" && \
        rm "$video_clean" && \
        mv "${video_clean%.*}.compressed.mp4" "${video_clean%.*}.mp4"
    done

elif [[ "$1" == "audio" ||  "$2" == "audio" || "$3" == "audio" ]]; then
    # Process audio files (WAV, FLAC, MP3, OGG)
    find ./src -name "*.wav" -o -name "*.flac" -o -name "*.mp3" -o -name "*.ogg" | while read -r audio; do
        audio_clean="${audio#./}" # Remove './' prefix
        ffmpeg -i "$audio" -c:a libopus -b:a 96k "${audio_clean%.*}.opus" && \
        git rm --cached "$audio_clean" && \
        echo "$audio_clean" >> "$temp_file" && \
        rm "$audio_clean"
    done

else
    echo "Usage: optimizer.zsh <image|video|audio>"
    exit 1
fi

# Rewrite git history for all stored paths
if [[ -s "$temp_file" ]]; then
    git filter-repo --invert-paths --paths-from-file "$temp_file" --force
fi

# Cleanup temporary file
rm "$temp_file"

