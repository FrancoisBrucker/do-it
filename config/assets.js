// const postCSSConfig = require("eleventy-postcss-extension");

export default function (eleventyConfig) {

  // eleventyConfig.addPlugin(postCSSConfig);

  // garder le node_modules des assets, ignorer les autres
  eleventyConfig.addPassthroughCopy("src/assets/node_modules");
  eleventyConfig.ignores.add("src/!(assets)/**/node_modules");

  // images 
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{jpg,png,ico,pdf,svg,gif,webp}");

  // videos
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{webm,mov,mp4,ogv}");
  
  // data
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{txt,edi,csv,json,pdf,zip}");

};
