import tippy, { TippyPluginOptions } from "vue-tippy";
import "tippy.js/dist/tippy.css";
import "./tippy.scss";

const options: TippyPluginOptions = {
  directive: "tooltip",
  component: "tooltip",
  defaultProps: {
    delay: [300, 0],
    duration: 200,
    offset: [13, 13],
    allowHTML: true,
    onAfterUpdate: (instance): void => {
      /**
       * if tooltip target/reference is plain text (not link, not button, etc), add
       * styling to indicate it has tooltip
       */
      if (instance.reference.tagName === "SPAN" && !!instance.props.content)
        instance.reference.setAttribute("data-tooltip", "true");
    },
    appendTo: () => document.body,
    /** cancel show if no content to show */
    onShow: (instance) => {
      if (!String(instance.props.content).trim()) return false;
    },
    onHide: () => {
      /** return false to keep open for debugging */
      // return false
    },
  },
};

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(tippy, options);
});
