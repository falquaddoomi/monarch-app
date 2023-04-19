import { init, vueRouterInstrumentation } from "@sentry/vue";
import { BrowserTracing } from "@sentry/browser";

/** track app errors */

export default defineNuxtPlugin((nuxtApp) => {
  if (process.env.NODE_ENV === "production")
    init({
      app: nuxtApp.vueApp,
      dsn: "https://122020f2154c48fa9ebbc53b98afdcf8@o1351894.ingest.sentry.io/6632682",
      integrations: [
        new BrowserTracing({
          routingInstrumentation: vueRouterInstrumentation(useRouter()),
        }),
      ],
      tracesSampleRate: 1.0,
      logErrors: true,
      environment: process.env.NODE_ENV,
    });
});
