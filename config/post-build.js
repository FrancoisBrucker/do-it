import { execSync } from "child_process";

export default function (eleventyConfig) {

    eleventyConfig.on('eleventy.after', () => {
        execSync(`tailwindcss -i ./src/assets/stylesheets/main.css -o ./dist/assets/stylesheets/main.css`)
    })

    // Search config with pagefind
    eleventyConfig.on('eleventy.after', () => {
        execSync(`npx pagefind --site dist --glob \"**/*.html\"`, { encoding: 'utf-8' })
    })
}