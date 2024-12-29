import { EleventyRenderPlugin, EleventyHtmlBasePlugin } from "@11ty/eleventy";
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";
import syntaxHighlight from "@11ty/eleventy-plugin-syntaxhighlight";
import setupMarkdown from './config/markdown/index.js';
import setupShortcodes from "./config/markdown/shortcodes/index.js";
import assetsConfig from "./config/assets.js";
import filtersConfig from "./config/filters.js";
import postCompilation from "./config/post-build.js";
import replaceMediaSource from "./config/media-githubusercontent.js";

export default function(eleventyConfig) {

  // Compute eleventyNavigationBreadcrumb only in production (significant performance gain)
  eleventyConfig.addGlobalData("navigation", process.env.NODE_ENV === "production" || process.env.NAV === "true");

  if (process.env.GITHUB_ACTIONS) {
    replaceMediaSource(eleventyConfig, `https://raw.githubusercontent.com/${process.env.GITHUB_REPOSITORY}/${process.env.GITHUB_SHA}`)
  } else if (process.env.STATIC_MEDIA_LINKS) {
    replaceMediaSource(eleventyConfig, `https://raw.githubusercontent.com/FrancoisBrucker/do-it/refs/heads/main`)
  }

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);
  eleventyConfig.addPlugin(syntaxHighlight);

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
