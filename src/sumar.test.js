import { sumar } from "./sumar";
import { expect, test } from "vitest";

test("sumar 1 + 1 es 2", () => {
  expect(sumar(1, 1)).toBe(2);
});
