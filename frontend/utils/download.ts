/** download json data as json file */
export const downloadJson = (data = {}, filename = "data"): void => {
  const blob = new Blob([stringify(data, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const link = document?.createElement("a");
  link.href = url;
  link.download = filename + ".json";
  link.click();
  URL.revokeObjectURL(url);
};
