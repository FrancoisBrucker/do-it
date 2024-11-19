import {DateTime} from "luxon";

export default async function(eleventyConfig) {

    eleventyConfig.addCollection("promos", function(collectionApi) {
        return collectionApi.getFilteredByGlob("./src/promos/!(20XX-20YY)/index.njk");
    });

    eleventyConfig.addFilter("siteUrl", function (url, base="/") {
        try {
            if (Array.isArray(url)) {
                let r = [];
                let x;
                for (x of url) {
                    r.push(decodeURI(new URL(x, new URL(base, "http://localhost/").href).toString()).substring(16));
                }

                return r
            } else {
              return decodeURI(new URL(url, new URL(base, "http://localhost/").href).toString()).substring(16);
            }
        } catch (err) {
            console.error(err);
            return url;
            }
    });

    eleventyConfig.addFilter('getValueFromPath', function(str, separator, value) {
        return str.split(new RegExp(separator))[value];
    });

    eleventyConfig.addFilter("HalfTimeFromUrl", (url) => {
        if (url.endsWith(`.1/`)) {
            return `.1`;
        } else if (url.endsWith(`.2/`)) {
            return `.2`;
        }
        else return undefined
    });

    eleventyConfig.addFilter("dateFormat", (dateObj, format = "dd/MM/yyyy") => {
        return DateTime.fromJSDate(dateObj).toFormat(format);
    });

  };
