
const outdent = require('outdent');

module.exports = function (markdownItLibrary, eleventyConfig) {

    eleventyConfig.addPairedShortcode('details', (content, arg) => {
        summary = `<summary>${arg}</summary>`
        content = outdent`${markdownItLibrary.render(content)}` 

        return '<details>' + summary + content + '</details>'
    });
};

