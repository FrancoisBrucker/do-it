function extractExcerpt(content) {
  // Original https://keepinguptodate.com/pages/2019/06/creating-blog-with-eleventy/
  // console.warn(content.templateContent)
  return "Résumé"
}

export default function(eleventyConfig) {
  eleventyConfig.addShortcode('résumé', function (content) {
     console.warn(content.templateContent)
  })
};
