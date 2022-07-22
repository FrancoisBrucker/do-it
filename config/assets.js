module.exports = function (eleventyConfig) {

  eleventyConfig.addPassthroughCopy("src/assets/");
  eleventyConfig.addPassthroughCopy("src/blog/**/*.jpg");

};

