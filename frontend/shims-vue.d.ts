/* eslint-disable */
/** generic typescript types for files */

declare module "phenogrid" {
  import type { PhenogridDefinition } from "@/api/phenogrid";
  const phenogrid: PhenogridDefinition;
  export default phenogrid;
}

declare module "*.mp4" {
  const path: string;
  export default path;
}
