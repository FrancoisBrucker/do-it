
module.exports = function (eleventyConfig) {

    require('./details')(eleventyConfig);
    require('./exercice')(eleventyConfig);
    require('./note')(eleventyConfig);
    require('./chemin')(eleventyConfig);
    require('./attention')(eleventyConfig);
    require('./lien')(eleventyConfig);
    require('./prerequis')(eleventyConfig);
    require('./info')(eleventyConfig);
    require('./faire')(eleventyConfig);
};

