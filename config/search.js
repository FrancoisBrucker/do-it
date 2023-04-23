const { execSync } = require('child_process')

module.exports = function (eleventyConfig) {
    eleventyConfig.on('eleventy.after', () => {
        execSync(`npx pagefind --source dist --glob \"**/*.html\"`, { encoding: 'utf-8' })
    })
}