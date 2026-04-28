---
slug: sprite-sheet-background-cleanup
title: Sprite Sheet Background Cleanup
summary: Convert chosen source frames into transparent, same-canvas sprite sheets without keying out character details that share the background color.
tags:
  - games
  - assets
  - sprites
  - image-processing
triggers:
  - Source sprite frames need background removal before game import.
  - The background color is also used inside the character, such as black eyes, glasses, outlines, shoes, or hair.
  - A runtime sprite sheet must preserve exact selected frames, frame order, canvas size, and baseline alignment.
inputs:
  - Exact source frame folder and expected frame count.
  - Target frame size, sheet orientation, and runtime asset path.
  - Existing game code or docs that define frame count, slice size, FPS, and import path.
outputs:
  - Cleaned transparent per-frame PNGs when useful for source traceability.
  - Runtime sprite sheet with verified dimensions and alpha channel.
  - Matching runtime frame-count/code updates and any small source-grounded docs correction.
agent_behavior:
  - Treat user-selected frames as fixed input; do not add, drop, or reorder frames unless explicitly asked.
  - Prefer border-connected background removal over global chroma keying when the character contains the background color.
  - Verify visually and with image metadata before claiming the sheet is ready.
safety:
  - Do not globally remove every pixel matching the background color when that color may appear in eyes, glasses, outlines, shoes, hair, or clothing.
  - Do not leave old frame-count constants or asset-pipeline docs contradicting the new sheet dimensions.
status: active
version: 1.0.0
---

# Goal

Build game-ready sprite sheets from a fixed set of selected frames while preserving character details that share the background color. The common failure this prevents is using a naive black/green/white chroma key that also deletes eyes, glasses, outlines, shoes, or other legitimate dark details.

## Use It When

- The user supplies final frame choices and asks for resizing, transparency, or sheet assembly.
- The source frames have a solid or near-solid background that also appears inside the character.
- Runtime code slices a sprite sheet by fixed frame size/count.
- The sheet must align feet or another baseline across frames.

## Do Not Use It When

- The source frames are already clean transparent PNGs.
- The task is only drawing or redesigning a character.
- The user wants a manual art pass in an editor rather than automated cleanup.
- The background is complex enough that automated edge-connected removal cannot be trusted without manual masking.

# Procedure

## 1. Confirm The Runtime Contract

Inspect the repo before processing:

- source frame folder and exact frame count
- current runtime sprite path
- target frame size and sheet orientation
- frame-count constants or animation metadata
- docs that state required dimensions

Use the user's chosen frames exactly. If the expected count and discovered count disagree, stop before generating output.

## 2. Separate Foreground From Source Noise

Detect the main character region before removing the background:

- identify non-background connected components
- keep the components that belong to the character
- exclude watermarks, UI labels, or unrelated source artifacts
- crop around the character with a small margin

Do not crop from all non-background pixels blindly if the source contains a watermark or capture overlay.

## 3. Remove Only Edge-Connected Background

Use border-connected background removal instead of a global color key:

- classify near-background-color pixels as background candidates
- flood-fill only candidates connected to the crop border
- protect pixels adjacent to confirmed foreground with a small dilation radius
- make only the flood-filled background transparent

This keeps internal black/dark details opaque while still clearing the exterior background and open spaces.

## 4. Resize And Align

Normalize frames into the target canvas:

- compute a shared scale from the largest cleaned frame
- preserve relative size across the cycle
- place each frame on the same baseline
- keep transparent borders around every frame
- assemble the sheet in the required order and orientation

For horizontal sheets, final width should equal `frame_width * frame_count`.

## 5. Update Runtime References

If the frame count or dimensions changed, update the smallest necessary runtime references:

- frame-count constants
- animation metadata
- asset-pipeline notes that would otherwise become stale

Do not redesign animation timing unless the user requested it or the existing code cannot play the new sheet correctly.

## 6. Verify Before Handoff

Run image and app checks:

- file metadata confirms expected sheet size and RGBA alpha
- each slice is the target frame size
- frame borders are transparent
- each frame still contains opaque pixels matching protected dark details
- the app builds or the relevant asset loader succeeds
- a visual preview shows no black rectangle around the character

If using a live game preview, capture at least one screenshot from the actual runtime surface.

# Success Criteria

- The final sheet uses exactly the selected frames in order.
- The final dimensions match the runtime contract.
- The character's dark details remain visible after transparency cleanup.
- The background is transparent, including frame borders.
- Runtime code slices the new frame count correctly.
- The sheet frame size is large enough for the intended render size, so the game is not enlarging a tiny source frame until it looks soft or blurry.

# Common Failure Modes

- Global color keying deletes eyes, outlines, shoes, glasses, or other character details that match the background color.
- Cropping includes source watermarks or UI overlays because all non-background pixels were treated as foreground.
- Frames are assembled with the right image content but the wrong runtime count, dimensions, or order.
- The character shifts vertically because each frame was centered independently instead of aligned to a shared baseline.
- The sheet looks correct as an image file but fails in-game because the app still slices the old frame size or old frame count.

# Example Prompt

"Use `sprite-sheet-background-cleanup` on these selected source frames. Preserve the exact frame order, remove only edge-connected background, keep dark character details intact, build the runtime sprite sheet at the required frame size, update any frame-count references, and verify the sheet dimensions plus an actual game preview."
