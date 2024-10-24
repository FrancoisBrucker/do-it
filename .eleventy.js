import { EleventyRenderPlugin, EleventyHtmlBasePlugin } from "@11ty/eleventy"
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";
import setupMarkdown from './config/markdown/index.js';
import setupShortcodes from "./config/markdown/shortcodes/index.js"
import assetsConfig from "./config/assets.js"
import filtersConfig from "./config/filters.js";
import postCompilation from "./config/search.js"

export default function(eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  setupMarkdown(eleventyConfig);
  setupShortcodes(eleventyConfig);
  assetsConfig(eleventyConfig);
  filtersConfig(eleventyConfig);
  postCompilation(eleventyConfig); // tailwind and search

  return {
    dir: {
      input: "src",
      output: "dist",
    },
    markdownTemplateEngine: "njk",
  };
};
