
module.exports = function (eleventyConfig) {
    // https://stackoverflow.com/questions/72183639/how-to-create-a-tags-collection-and-a-categories-collection-in-eleventy

    // Tags
    eleventyConfig.addCollection('tagList', collection => {
        const tagsSet = {};
        //console.log(collection)
        collection.getAll().forEach(item => {
            
            if (!item.data.tags) return;
            item.data.tags.filter(
                tag => !['posts', 'all'].includes(tag)
            ).forEach(
                tag => {
                    if (!tagsSet[tag]) { tagsSet[tag] = []; }
                    tagsSet[tag].push(item)
                }
            );
        });
        //console.log(tagsSet)
        return tagsSet;
    });
}