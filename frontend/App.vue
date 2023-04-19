<!--
  entry point for entire app
-->

<template>
  <Head>
    <!-- basic  -->
    <Title>{{ config.public.TITLE }}</Title>
    <Meta name="title" :content="config.public.title" />
    <Meta name="description" :content="config.public.description" />

    <!-- favicons -->
    <Link
      rel="icon"
      type="image/png"
      sizes="512x512"
      href="favicon-512x512.png"
    />
    <Link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png" />
    <Link rel="manifest" href="site.webmanifest" />
    <Link rel="mask-icon" href="safari-pinned-tab.svg" color="#00838f" />
    <Meta name="msapplication-TileColor" content="#00838f" />
    <Meta name="theme-color" content="#ffffff" />

    <!-- open graph -->
    <Meta property="og:type" content="website" />
    <Meta property="og:url" :content="config.public.url" />
    <Meta property="og:title" :content="config.public.title" />
    <Meta property="og:description" :content="config.public.description" />
    <Meta property="og:image" content="share.jpg" />

    <!-- twitter -->
    <Meta property="twitter:card" content="summary_large_image" />
    <Meta property="twitter:url" :content="config.public.url" />
    <Meta property="twitter:title" :content="config.public.title" />
    <Meta property="twitter:description" :content="config.public.description" />
    <Meta property="twitter:image" content="share.jpg" />

    <!-- extra -->
    <Link rel="canonical" :href="config.public.url" />
    <Meta name="robots" content="index, follow" />

    <!-- fonts -->
    <Link rel="preconnect" href="https://fonts.googleapis.com" />
    <Link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <Link
      href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap"
      rel="stylesheet"
    />
    <Link
      href="https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap"
      rel="stylesheet"
    />
  </Head>

  <Body>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </Body>
</template>

<script setup lang="ts">
import "normalize.css";
import "@/global/icons";
import "@/global/styles.scss"; /** keep these styles last so they take priority */
import "wicg-inert";

// const { setupWorker } = await import("msw");
// const { handlers } = await import("@/tests/fixtures");
// await setupWorker(...handlers).start();

const config = useRuntimeConfig();

useHead({
  script: [
    /** json linked data spec */
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify([
        {
          "@context": "http://schema.org",
          "@type": "Organization",
          url: "https://monarchinitiative.org",
          email: "info@monarchinitiative.org",
        },
        {
          "@context": "http://schema.org",
          "@type": "WebSite",
          url: "https://monarchinitiative.org",
          potentialAction: {
            "@type": "SearchAction",
            target: "https://monarchiniative.org/explore/?search={term}",
            "query-input": "required name=term",
          },
        },
      ]),
    },
  ],
});
</script>
