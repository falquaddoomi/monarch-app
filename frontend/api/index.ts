/**
 * base api url
 */
export const biolink = "https://api.monarchinitiative.org/api";
export const monarch = "https://api-dev.monarchinitiative.org/api";
// export const monarch = "http://127.0.0.1:8000/api";

/**
 * key/value object for request query parameters. use primitive for single, e.g.
 * evidence=true. use array for multiple/duplicate, e.g. id=abc&id=def&id=ghi
 */
type Param = string | number | boolean | undefined | null;
export type Params = Record<string, Param | Array<Param>>;

/**
 * generic fetch request wrapper
 *
 * @param path request url
 * @param params url params
 * @param options fetch() options
 * @param parse parse response mode
 */
export const request = async <T>(
  path = "",
  params: Params = {},
  options: RequestInit = {},
  parse: "text" | "json" = "json"
): Promise<T> => {
  /** get string of url parameters/options */
  const paramsObject = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    const values = [value].flat();
    for (const value of values)
      if (["string", "number", "boolean"].includes(typeof value))
        paramsObject.append(key, String(value));
  }

  /** sort params for consistency */
  paramsObject.sort();

  /** assemble url to query */
  const paramsString = "?" + paramsObject.toString();
  const url = path + paramsString;
  const endpoint = path.replace(biolink, "");

  /** make request object */
  const request = new Request(url, options);

  /** log details for debugging (except don't clutter logs when running tests) */
  if (process.env.NODE_ENV !== "test") {
    // console.groupCollapsed("📞 Request", endpoint);
    // console.info({ params, options, request });
    // console.groupEnd();
  }

  /** make new request */
  const response = await fetch(url, options);

  /** check response code */
  if (!response.ok) {
    /** get biolink error message, if there is one */
    let message;
    try {
      message = ((await response.json()) as _Error).error.message;
    } catch (error) {
      message = "";
    }
    throw new Error(message || `Response not OK`);
  }

  /** parse response */
  const parsed =
    parse === "text"
      ? ((await response.text()) as unknown as T)
      : await response.json();

  /** log details for debugging (except don't clutter logs when running tests) */
  if (process.env.NODE_ENV !== "test") {
    // console.groupCollapsed("📣 Response", endpoint);
    // console.info({ parsed, response });
    // console.groupEnd();
  }

  return parsed;
};

/** possible biolink error */
interface _Error {
  error: {
    message: string;
  };
}
