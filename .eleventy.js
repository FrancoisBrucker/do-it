import { EleventyRenderPlugin, EleventyHtmlBasePlugin } from "@11ty/eleventy"
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";
import setupMarkdown from './config/markdown/index.js';
import setupShortcodes from "./config/markdown/shortcodes/index.js"
import assetsConfig from "./config/assets.js"
import collectionsConfig from "./config/filters.js";

export default function(eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);

  // eleventyConfig.addPlugin(embedYouTube);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  setupMarkdown(eleventyConfig);
  setupShortcodes(eleventyConfig);
  assetsConfig(eleventyConfig);
  collectionsConfig(eleventyConfig);

  // markdownConfig(eleventyConfig);
  // searchConfig(eleventyConfig);

  eleventyConfig.addFilter('getValueFromPath', function(str, separator, value) {
    return str.split(new RegExp(separator))[value];
  });

  return {
    dir: {
      input: "src",
      output: "dist",
    },
    markdownTemplateEngine: "njk",
  };
};
