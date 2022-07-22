const markdownIt = require("markdown-it");
const markdownItAttrs = require('markdown-it-attrs');

const syntaxHighlight = require('@pborenstein/eleventy-md-syntax-highlight')
const mathjaxPlugin = require("eleventy-plugin-mathjax");

const shortcode = require("./shortcodes")

module.exports = function (eleventyConfig) {

    markdownItLibrary = markdownIt({
        html: true,
        breaks: true,
        linkify: true
    })
    
    markdownItLibrary.use(markdownItAttrs)

    eleventyConfig.setLibrary("md", markdownItLibrary);
    
    eleventyConfig.addPlugin(syntaxHighlight, 
      { showLineNumbers: false }
    );
    eleventyConfig.addPlugin(mathjaxPlugin);

    shortcode(markdownItLibrary, eleventyConfig);

};

