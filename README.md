# STL Watermarker – Blender Add-on

**STL Watermarker** is a lightweight Blender add-on developed by [WarfareWorkshop](https://warfareworkshop.com) that allows you to easily insert traceable watermarks (text-based) into 3D models before exporting them as `.stl`, `.obj`, or `.fbx` files.

This tool is especially useful for:
- Creators who distribute STL files and want to track file provenance.
- Designers aiming to deter piracy with subtle, embedded identifiers.
- Sellers who want to embed customer/order IDs into distributed models.

## ✨ Features

- 🧩 Insert custom text as a watermark into selected 3D models.
- 🔄 Automatically converts text into geometry and merges it with the model.
- 📦 Designed for STL distribution but works with all Blender-supported export formats.
- 🎛️ Simple UI integration: available in the **Watermark** tab of the 3D View sidebar.
- 🔐 Ideal for forensic traceability and anti-piracy measures.

## 🧰 Requirements

- Blender 2.90 or higher  
- Python (included with Blender)

## 📦 Installation

1. Download the `stl_watermarker.py` file (or copy from this repository).
2. Open Blender, go to **Edit > Preferences > Add-ons > Install**.
3. Select the Python file and enable the checkbox to activate it.
4. You’ll find a new **Watermark** tab in the 3D View's right-hand toolbar (`N` key).

## 📝 How to Use

1. Open or import your model in Blender.
2. Select the mesh object you want to watermark.
3. Open the **Watermark** tab in the sidebar.
4. Enter the text you want to embed (e.g., `WW2025-ID001`).
5. Click **“Add Watermark”**.
6. The text will be converted into geometry and merged with your model.
7. Export the model as usual via **File > Export > STL/OBJ/FBX**.

## 🔧 Example Use Case

You sell STL packs online and want to discourage file sharing. With this add-on, you can:
- Embed a unique identifier (like a buyer’s order number) into each file.
- Keep the mark small and hidden inside the base of the model.
- Detect unauthorized redistribution by checking which file ID appears.

## 📌 Notes

- The current version embeds the watermark at the origin `(0, 0, 0)`. You may need to reposition it depending on your model.
- This add-on does **not** include DRM or encryption — it's a soft watermarking tool.
- Designed for ease of use and batch watermarking workflows in future versions.

## 🛠️ Roadmap

- [ ] Batch processing for folders of models
- [ ] Auto-positioning under the base of miniatures
- [ ] Support for watermarking via mesh deformation
- [ ] Metadata-based watermarking (for formats that support it)
- [ ] Export presets with watermark baked in

## 🤝 License

GPLv3 License — Free to use, modify, and distribute.

## 👨‍💻 Author

**David @ WarfareWorkshop**  
https://warfareworkshop.com  
