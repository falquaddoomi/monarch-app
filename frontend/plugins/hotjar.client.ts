import Hotjar from "vue-hotjar";

/** track user usage and behavior */

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(Hotjar, {
    id: "3100256",
    isProduction: process.env.NODE_ENV === "production",
  });
});
