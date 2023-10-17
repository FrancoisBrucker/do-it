module.exports = function (eleventyConfig) {

  eleventyConfig.addPlugin(require("eleventy-postcss-extension"));

  // garder le node_modules des assets, ignorer les autres
  eleventyConfig.addPassthroughCopy("src/assets/node_modules");
  eleventyConfig.ignores.add("src/!(assets)/**/node_modules");

  // images 
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{jpg,png,ico,pdf,svg,gif}");

  // videos
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{webm,mov,mp4,ogv}");
  
  // data
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{txt,edi,csv,json,pdf,zip}");

};

