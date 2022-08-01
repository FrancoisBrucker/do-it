
const outdent = require('outdent');

module.exports = function (markdownItLibrary, eleventyConfig) {

    eleventyConfig.addPairedShortcode('exercice', (content) => {
        content = "<div>" + outdent`${markdownItLibrary.render(content)}` + "</div>"

        return '<div class="exercice">' + content + '</div>'
    });
};

