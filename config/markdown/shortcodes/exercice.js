
const { escapeHtml } = require("./utils")

module.exports = function (eleventyConfig) {

    eleventyConfig.addPairedShortcode('exercice', (content, arg) => {
        content = escapeHtml("<div>") + `${content}` + escapeHtml("</div>")

        return escapeHtml('<div class="exercice">') + content + escapeHtml('</div>')
    });
};



