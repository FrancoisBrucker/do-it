import { EleventyRenderPlugin, EleventyHtmlBasePlugin } from "@11ty/eleventy"
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";
import setupMarkdown from './config/markdown/index.js';
import setupShortcodes from "./config/markdown/shortcodes/index.js"
import assetsConfig from "./config/assets.js"
import searchConfig from "./config/search.js"
import collectionsConfig from "./config/filters.js";
import { DateTime } from "luxon";

export default function(eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);

  // eleventyConfig.addPlugin(embedYouTube);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  setupMarkdown(eleventyConfig);
  setupShortcodes(eleventyConfig);
  assetsConfig(eleventyConfig);
  collectionsConfig(eleventyConfig);
  searchConfig(eleventyConfig);

  eleventyConfig.addFilter('getValueFromPath', function(str, separator, value) {
    return str.split(new RegExp(separator))[value];
  });

  eleventyConfig.addFilter("dateFormat", (dateObj, format = "dd/MM/yyyy") => {
    return DateTime.fromJSDate(dateObj).toFormat(format);
  });

  return {
    dir: {
      input: "src",
      output: "dist",
    },
    markdownTemplateEngine: "njk",
  };
};
