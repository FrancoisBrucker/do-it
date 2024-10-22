export default async function(eleventyConfig) {

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

  };
