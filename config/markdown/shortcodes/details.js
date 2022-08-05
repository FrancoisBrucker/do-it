
const { escapeHtml } = require("./utils")

module.exports = function (eleventyConfig) {

    eleventyConfig.addPairedShortcode('details', (content, arg) => {
        
        summary = escapeHtml("<summary>") + `${arg}` + escapeHtml("</summary>")
        content = escapeHtml("<div>") +`${content}` + escapeHtml("</div>")

        return escapeHtml('<details>') + summary + content + escapeHtml('</details>')
    });
};

