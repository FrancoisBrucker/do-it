import path from "path";
import urls from "@11ty/posthtml-urls";

export default function (eleventyConfig, githubusercontentBase) {

    function mediaUrlTransform(context) {
        const urls_options = {
            eachURL: function (url, attr, tagName) {
                if (url.includes("://")) return url; // Don't transform external URLs
                    if (url.startsWith("/")) { // Absolute url, unused at the time of writing and somewhat annoying to deal with, skip for now
                        console.log(url);
                        return url;
                    } else { // Hopefully valid relative URL
                        return `${githubusercontentBase}/${path.dirname(context.inputPath)}/${url}`;
                    }
            },
            filter: {
                img: { src: true, srcset: true },
                video: { src: true, srcset: true },
                audio: { src: true },
                source: { src: true, srcset: true }
            }

        }
        return urls(urls_options);
    }

    eleventyConfig.htmlTransformer.addPosthtmlPlugin("html", mediaUrlTransform, {priority: -1});
}
