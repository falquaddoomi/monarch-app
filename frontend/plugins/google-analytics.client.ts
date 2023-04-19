import VueGtag, { trackRouter } from "vue-gtag-next";

/** track app usage */

export default defineNuxtPlugin((nuxtApp) => {
  if (process.env.NODE_ENV === "production") {
    nuxtApp.vueApp.use(VueGtag, {
      property: {
        id: "G-RDNWN51PE8",
      },
    });
    trackRouter(useRouter());
  }
});
