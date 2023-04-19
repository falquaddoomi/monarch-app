// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: true,

  runtimeConfig: {
    public: {
      TITLE: "Monarch Initiative",
      DESCRIPTION:
        "The Monarch Initiative integrates, aligns, and re-distributes cross-species gene, genotype, variant, disease, and phenotype data.",
      URL: "https://monarchinitiative.org/",
    },
  },

  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "@/global/variables.scss" as *;',
        },
      },
    },
  },
});
