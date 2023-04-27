const { EleventyRenderPlugin } = require("@11ty/eleventy");
const { EleventyHtmlBasePlugin } = require("@11ty/eleventy");

const embedYouTube = require("eleventy-plugin-youtube-embed");
const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");

const markdownConfig = require("./config/markdown")
const assetsConfig = require("./config/assets")
const searchConfig = require("./config/search")


module.exports = function (eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
  
  eleventyConfig.addPlugin(embedYouTube);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);
  
  markdownConfig(eleventyConfig);
  assetsConfig(eleventyConfig);
  searchConfig(eleventyConfig);

  eleventyConfig.addFilter('getValueFromPath', function(str, separator, value) {
    return str.split(new RegExp(separator))[value];
  });

  return {
    dir: {
      input: "src",
      output: "dist"
    },
    markdownTemplateEngine: "njk",
  }

};