const moment = require('moment');
moment.locale('fr');

const markdownIt = require("markdown-it");
const markdownItAttrs = require('markdown-it-attrs');

// const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const syntaxHighlight = require('@pborenstein/eleventy-md-syntax-highlight')

module.exports = function (eleventyConfig) {
 
  eleventyConfig.addFilter('dateIso', date => {
    return moment(date).toISOString();
  });
 
  eleventyConfig.addFilter('dateReadable', date => {
    return moment(date).utc().format('LL'); // E.g. May 31, 2019
  });

  eleventyConfig.addShortcode('excerpt', article => extractExcerpt(article));

  eleventyConfig.addPlugin(syntaxHighlight, 
    { showLineNumbers: false });

  markdownItLibrary = markdownIt({
    html: true,
    breaks: true,
    linkify: true
  })
  
  markdownItLibrary.use(markdownItAttrs)
  
  
  eleventyConfig.setLibrary("md", markdownItLibrary);

  eleventyConfig.addPassthroughCopy("sources/node_modules");

  return {
    pathPrefix: "/do-it/",
    dir: {
      input: "sources"
    },
  }

};

function extractExcerpt(article) {
  if (!article.hasOwnProperty('templateContent')) {
    console.warn('Failed to extract excerpt: Document has no property "templateContent".');
    return null;
  }
 
  let excerpt = null;
  const content = article.templateContent;
 
  // The start and end separators to try and match to extract the excerpt
  const separatorsList = [
    { start: '<!-- résumé : début -->', end: '<!-- résumé : fin -->' },
    { start: '<p>', end: '</p>' }
  ];
 
  separatorsList.some(separators => {
    const startPosition = content.indexOf(separators.start);
    const endPosition = content.indexOf(separators.end);
 
    if (startPosition !== -1 && endPosition !== -1) {
      excerpt = content.substring(startPosition + separators.start.length, endPosition).trim();
      return true; // Exit out of array loop on first match
    }
  });
 
  return excerpt;
}
