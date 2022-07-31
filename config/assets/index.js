

const stylesheetsConfig = require("./stylesheets")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPassthroughCopy("src/assets/node_modules");

  eleventyConfig.addPassthroughCopy("src/blog/**/*.jpg");

  stylesheetsConfig(eleventyConfig)

};

