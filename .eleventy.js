const markdownConfig = require("./config/markdown")

const assetsConfig = require("./config/assets")

module.exports = function (eleventyConfig) {

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