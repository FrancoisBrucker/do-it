import { execSync } from "child_process";

export default function (eleventyConfig) {
    eleventyConfig.on('eleventy.after', () => {
        execSync(`npx pagefind --source dist --glob \"**/*.html\"`, { encoding: 'utf-8' })
    })
}