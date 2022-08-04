const { EleventyRenderPlugin } = require("@11ty/eleventy");

const markdownConfig = require("./config/markdown")
const assetsConfig = require("./config/assets")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);

  markdownConfig(eleventyConfig);
  assetsConfig(eleventyConfig);

  return {
    pathPrefix: "/do-it/",
    dir: {
      input: "src",
      output: "dist"
    },
  }

};