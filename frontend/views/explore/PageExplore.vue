<!--
  explore landing page
-->

<template>
  <AppSection>
    <AppHeading>Explore</AppHeading>

    <AppTabs v-model="tab" name="Explore Mode" :tabs="tabs" />
  </AppSection>

  <NodeSearch v-if="tab === 'node-search'" />

  <TextAnnotator v-if="tab === 'text-annotator'" />

  <PhenotypeExplorer v-if="tab === 'phenotype-explorer'" />
</template>

<script setup lang="ts">
import { startCase } from "lodash-es";
import AppTabs from "@/components/AppTabs.vue";
import NodeSearch from "./NodeSearch.vue";
import TextAnnotator from "./TextAnnotator.vue";
import PhenotypeExplorer from "./PhenotypeExplorer.vue";
import tabs from "../../pages/explore/tabs.json";

/** route info */
const route = useRoute();

/** selected tab */
const tab = ref(tabs[0].id);

/** update document title */
useHead({
  title: () => startCase(route.hash),
});
</script>
