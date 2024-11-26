import info from "./info.js";
import attention from "./attention.js";
import note from "./note.js";
import faire from "./faire.js";
import details from "./details.js";
import exercice from "./exercice.js";
import chemin from "./chemin.js";
import prerequis from "./prerequis.js";
import lien from "./lien.js";
import lieninterne from "./lieninterne.js";

export default async function(eleventyConfig) {

    info(eleventyConfig);
    attention(eleventyConfig);
    note(eleventyConfig);
    faire(eleventyConfig);
    details(eleventyConfig);
    exercice(eleventyConfig);
    chemin(eleventyConfig);
    prerequis(eleventyConfig);
    lien(eleventyConfig);
    lieninterne(eleventyConfig);

}
