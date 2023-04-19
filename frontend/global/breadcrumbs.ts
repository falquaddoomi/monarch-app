import { Node } from "@/api/node-lookup";
import { Association } from "@/api/node-associations";

interface Breadcrumb {
  node: Node;
  relation: Association["relation"];
}

/** breadcrumbs object for breadcrumbs section on node page */
export const breadcrumbs = useState<Array<Breadcrumb>>("breadcrumbs", () => []);

/** keep breadcrumbs global variable in sync with history.state.breadcrumbs */
export const updateBreadcrumbs = () =>
  (breadcrumbs.value = parse(history.state?.breadcrumbs, []));
