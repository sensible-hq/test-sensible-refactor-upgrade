// Check for broken links in the docs
await $`npx mintlify broken-links`.pipe(process.stdout);
