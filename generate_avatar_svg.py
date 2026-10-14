import base64

def generate():
    with open('assets/avatar_optimized.png', 'rb') as f:
        b64_img = base64.b64encode(f.read()).decode('utf-8')

    svg_content = f'''<svg width="800" height="1000" viewBox="0 0 800 1000" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Soft Warm Light & Golden Glow Filters -->
    <filter id="warmGlow" x="-50%" y="-300%" width="200%" height="700%">
      <feGaussianBlur stdDeviation="4" result="blur1" />
      <feGaussianBlur stdDeviation="10" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2" />
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="ambientSoftBlur" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="95" />
    </filter>

    <filter id="subtleAura" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="60" />
    </filter>

    <!-- Deep Obsidian / Charcoal Base Background -->
    <linearGradient id="cardBg" x1="0" y1="0" x2="800" y2="1000" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#090a0d" />
      <stop offset="50%" stop-color="#121318" />
      <stop offset="100%" stop-color="#07080a" />
    </linearGradient>

    <!-- Delicate Warm Champagne / Amber Border Gradient -->
    <linearGradient id="borderGrad" x1="0" y1="0" x2="800" y2="1000" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.5" />
      <stop offset="30%" stop-color="#f59e0b" stop-opacity="0.25" />
      <stop offset="70%" stop-color="#e0d650" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.45" />
    </linearGradient>

    <!-- Natural Warm Golden Ambient Aura (Champagne, Warm Gold & Subtle Amber) -->
    <radialGradient id="warmAura" cx="50%" cy="46%" r="48%" fx="50%" fy="44%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.38" />
      <stop offset="35%" stop-color="#e0d650" stop-opacity="0.26" />
      <stop offset="65%" stop-color="#d97706" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#121318" stop-opacity="0" />
    </radialGradient>

    <!-- Secondary Soft Fill Aura -->
    <radialGradient id="fillAura" cx="50%" cy="54%" r="52%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.16" />
      <stop offset="50%" stop-color="#b45309" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#090a0d" stop-opacity="0" />
    </radialGradient>

    <!-- Ultra-Faint Cinematic Scanline / Film Raster Interlace Texture -->
    <pattern id="filmRaster" width="100%" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="800" y2="0" stroke="#000000" stroke-width="1.1" stroke-opacity="0.12" />
    </pattern>

    <!-- Dynamic Raster Reveal ClipPath -->
    <clipPath id="rasterClip">
      <rect id="revealRect" x="0" y="0" width="800" height="0">
        <animate attributeName="height" from="0" to="1000" dur="2.5s" fill="freeze" calcMode="spline" keyTimes="0; 1" keySplines="0.25 0.9 0.3 1" />
      </rect>
    </clipPath>

    <!-- Outer Rounded Card Boundary -->
    <clipPath id="cardClip">
      <rect x="0" y="0" width="800" height="1000" rx="24" ry="24" />
    </clipPath>
  </defs>

  <style>
    @keyframes curtainSweep {{
      0% {{ height: 0px; }}
      100% {{ height: 1000px; }}
    }}

    @keyframes goldenSweep {{
      0% {{
        transform: translateY(0px);
        opacity: 1;
      }}
      88% {{
        opacity: 1;
      }}
      100% {{
        transform: translateY(1000px);
        opacity: 0;
      }}
    }}

    #revealRect {{
      animation: curtainSweep 2.5s cubic-bezier(0.25, 0.9, 0.3, 1) forwards;
    }}

    #scanlineBar {{
      animation: goldenSweep 2.5s cubic-bezier(0.25, 0.9, 0.3, 1) forwards;
    }}

    @media (prefers-reduced-motion: reduce) {{
      #revealRect {{ height: 1000px !important; animation: none !important; }}
      #scanlineBar {{ display: none !important; animation: none !important; }}
    }}
  </style>

  <!-- Card Frame and Atmosphere -->
  <g clip-path="url(#cardClip)">
    <!-- Deep Obsidian Matte Background -->
    <rect width="800" height="1000" fill="url(#cardBg)" />

    <!-- Atmospheric Warm Golden Ambient Lighting -->
    <circle cx="400" cy="450" r="360" fill="url(#warmAura)" filter="url(#ambientSoftBlur)" />
    <ellipse cx="400" cy="520" rx="300" ry="340" fill="url(#fillAura)" filter="url(#subtleAura)" />

    <!-- Reveal Group: Clipped Portrait & Delicate Film Texture -->
    <g clip-path="url(#rasterClip)">
      <!-- Portrait Image (Untouched original face, glasses, hand, camera, and patterned red outfit) -->
      <image
        href="data:image/png;base64,{b64_img}"
        x="25"
        y="15"
        width="750"
        height="1000"
        preserveAspectRatio="xMidYMid meet"
      />

      <!-- Ultra-Faint Cinematic Film Raster Interlace Texture -->
      <rect width="800" height="1000" fill="url(#filmRaster)" pointer-events="none" />
    </g>

    <!-- Sophisticated, Delicate Geometric Framing Markers (Warm Champagne / Soft Gold) -->
    <!-- Top-Left Corner Bracket -->
    <path d="M 28 44 L 28 28 L 44 28" fill="none" stroke="#e0d650" stroke-width="1.2" stroke-opacity="0.6" stroke-linecap="round" />
    <circle cx="28" cy="28" r="1.5" fill="#fef08a" fill-opacity="0.8" />

    <!-- Top-Right Corner Bracket -->
    <path d="M 772 44 L 772 28 L 756 28" fill="none" stroke="#e0d650" stroke-width="1.2" stroke-opacity="0.6" stroke-linecap="round" />
    <circle cx="772" cy="28" r="1.5" fill="#fef08a" fill-opacity="0.8" />

    <!-- Bottom-Left Corner Bracket -->
    <path d="M 28 956 L 28 972 L 44 972" fill="none" stroke="#e0d650" stroke-width="1.2" stroke-opacity="0.6" stroke-linecap="round" />
    <circle cx="28" cy="972" r="1.5" fill="#fef08a" fill-opacity="0.8" />

    <!-- Bottom-Right Corner Bracket -->
    <path d="M 772 956 L 772 972 L 756 972" fill="none" stroke="#e0d650" stroke-width="1.2" stroke-opacity="0.6" stroke-linecap="round" />
    <circle cx="772" cy="972" r="1.5" fill="#fef08a" fill-opacity="0.8" />

    <!-- Subtle Center-Edge Guide Marks -->
    <line x1="24" y1="500" x2="32" y2="500" stroke="#e0d650" stroke-width="1" stroke-opacity="0.35" />
    <line x1="768" y1="500" x2="776" y2="500" stroke="#e0d650" stroke-width="1" stroke-opacity="0.35" />

    <!-- Leading Edge Warm Light Reveal Bar (Delicate Golden Ambient Sweep) -->
    <g id="scanlineBar">
      <!-- Soft Amber Glow Diffusion -->
      <line x1="0" y1="0" x2="800" y2="0" stroke="#f59e0b" stroke-width="8" stroke-opacity="0.3" filter="url(#warmGlow)" />
      <!-- Warm Champagne Golden Beam -->
      <line x1="0" y1="0" x2="800" y2="0" stroke="#e0d650" stroke-width="2.5" stroke-opacity="0.75" filter="url(#warmGlow)" />
      <!-- Delicate Soft Light Core -->
      <line x1="0" y1="0" x2="800" y2="0" stroke="#fffbeb" stroke-width="1" stroke-opacity="0.9" />

      <!-- SMIL Animation for SVG Viewers -->
      <animateTransform attributeName="transform" type="translate" from="0,0" to="0,1000" dur="2.5s" fill="freeze" calcMode="spline" keyTimes="0; 1" keySplines="0.25 0.9 0.3 1" />
      <animate attributeName="opacity" values="1; 1; 0" keyTimes="0; 0.90; 1" dur="2.5s" fill="freeze" />
    </g>

    <!-- Ultra-Thin Minimalist Outer Frame -->
    <rect x="0.75" y="0.75" width="798.5" height="998.5" rx="23.25" ry="23.25" fill="none" stroke="url(#borderGrad)" stroke-width="1.2" />
  </g>
</svg>'''

    with open('assets/animated-avatar.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f'Done! Successfully generated minimalist warm golden animated avatar: {len(svg_content)} bytes ({round(len(svg_content)/1024)} KB)')

if __name__ == '__main__':
    generate()
