// news-image-20261121 — "Luminous Atlas" (Candidate A): 37 verified stories from 9 regions,
// Saturday 21 November 2026, rendered deterministically to a 1024x1024 PNG under 1 MiB.
// The program copies entry.png beside this file to /output/entry.png, after checking the
// competition's limits (at most 1024 by 1024 pixels, at most 1 MiB) from the PNG header
// itself, so an oversized image fails here instead of at the gate.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const src = new URL('./entry.png', import.meta.url);
const bytes = readFileSync(src);
if (bytes.length > 1024 * 1024) throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
// PNG signature, then width and height as big-endian uint32s at offsets 16 and 20.
const isPng =
  bytes.length >= 24 &&
  bytes.subarray(0, 8).equals(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]));
if (isPng) {
  const width = bytes.readUInt32BE(16);
  const height = bytes.readUInt32BE(20);
  if (width > 1024 || height > 1024) throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 limit`);
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
  mkdirSync(outDir, { recursive: true });
  const out = join(outDir, 'entry.png');
  copyFileSync(src, out);
  console.log(`wrote ${out} (${width}x${height}, ${statSync(out).size} bytes)`);
} else {
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
  mkdirSync(outDir, { recursive: true });
  const out = join(outDir, 'entry.png');
  copyFileSync(src, out);
  console.log(`wrote ${out} (${statSync(out).size} bytes)`);
}
