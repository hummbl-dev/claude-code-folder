#!/usr/bin/env python3
"""Generate Claude avatar SVGs."""
import os

os.makedirs("avatars", exist_ok=True)

COLOR = (
'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">\n'
'  <defs>\n'
'    <radialGradient id="orbGlow" cx="50%" cy="45%" r="40%">\n'
'      <stop offset="0%" stop-color="#C4B5FD" stop-opacity="0.9"/>\n'
'      <stop offset="50%" stop-color="#7C3AED"/>\n'
'      <stop offset="100%" stop-color="#5B21B6"/>\n'
'    </radialGradient>\n'
'    <radialGradient id="innerLight" cx="40%" cy="35%" r="30%">\n'
'      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.6"/>\n'
'      <stop offset="60%" stop-color="#7C3AED" stop-opacity="0.1"/>\n'
'      <stop offset="100%" stop-color="#5B21B6" stop-opacity="0"/>\n'
'    </radialGradient>\n'
'    <linearGradient id="rayIn1" x1="0%" y1="0%" x2="100%" y2="100%">\n'
'      <stop offset="0%" stop-color="#C4B5FD" stop-opacity="0"/>\n'
'      <stop offset="100%" stop-color="#C4B5FD" stop-opacity="0.6"/>\n'
'    </linearGradient>\n'
'    <linearGradient id="rayIn2" x1="100%" y1="0%" x2="0%" y2="100%">\n'
'      <stop offset="0%" stop-color="#C4B5FD" stop-opacity="0"/>\n'
'      <stop offset="100%" stop-color="#C4B5FD" stop-opacity="0.6"/>\n'
'    </linearGradient>\n'
'    <linearGradient id="rayIn3" x1="50%" y1="0%" x2="50%" y2="100%">\n'
'      <stop offset="0%" stop-color="#C4B5FD" stop-opacity="0"/>\n'
'      <stop offset="100%" stop-color="#C4B5FD" stop-opacity="0.5"/>\n'
'    </linearGradient>\n'
'    <linearGradient id="rayOut" x1="50%" y1="0%" x2="50%" y2="100%">\n'
'      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.8"/>\n'
'      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>\n'
'    </linearGradient>\n'
'    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">\n'
'      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>\n'
'      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>\n'
'    </filter>\n'
'    <filter id="outerGlow" x="-50%" y="-50%" width="200%" height="200%">\n'
'      <feGaussianBlur in="SourceGraphic" stdDeviation="12"/>\n'
'    </filter>\n'
'  </defs>\n'
'  <rect width="512" height="512" rx="64" fill="#1E1B4B"/>\n'
'  <circle cx="256" cy="256" r="220" fill="none" stroke="#2E2860" stroke-width="0.5" opacity="0.5"/>\n'
'  <circle cx="256" cy="256" r="190" fill="none" stroke="#2E2860" stroke-width="0.5" opacity="0.4"/>\n'
'  <circle cx="256" cy="256" r="160" fill="none" stroke="#2E2860" stroke-width="0.5" opacity="0.3"/>\n'
'  <line x1="60" y1="80" x2="210" y2="215" stroke="url(#rayIn1)" stroke-width="2.5" opacity="0.7"/>\n'
'  <line x1="452" y1="80" x2="302" y2="215" stroke="url(#rayIn2)" stroke-width="2.5" opacity="0.7"/>\n'
'  <line x1="50" y1="280" x2="195" y2="260" stroke="url(#rayIn1)" stroke-width="2" opacity="0.5"/>\n'
'  <line x1="462" y1="280" x2="317" y2="260" stroke="url(#rayIn2)" stroke-width="2" opacity="0.5"/>\n'
'  <line x1="256" y1="50" x2="256" y2="195" stroke="url(#rayIn3)" stroke-width="2.5" opacity="0.6"/>\n'
'  <line x1="120" y1="120" x2="220" y2="220" stroke="url(#rayIn1)" stroke-width="1.5" opacity="0.4"/>\n'
'  <line x1="392" y1="120" x2="292" y2="220" stroke="url(#rayIn2)" stroke-width="1.5" opacity="0.4"/>\n'
'  <polygon points="244,310 256,340 268,310 300,430 256,460 212,430" fill="url(#rayOut)" opacity="0.7"/>\n'
'  <line x1="256" y1="320" x2="256" y2="450" stroke="#F59E0B" stroke-width="3" opacity="0.5" filter="url(#softGlow)"/>\n'
'  <circle cx="256" cy="256" r="130" fill="#7C3AED" opacity="0.08" filter="url(#outerGlow)"/>\n'
'  <circle cx="256" cy="256" r="95" fill="url(#orbGlow)" filter="url(#softGlow)"/>\n'
'  <circle cx="240" cy="240" r="70" fill="url(#innerLight)"/>\n'
'  <g stroke="#C4B5FD" stroke-width="0.8" opacity="0.25">\n'
'    <line x1="175" y1="256" x2="337" y2="256"/>\n'
'    <line x1="256" y1="175" x2="256" y2="337"/>\n'
'    <line x1="198" y1="198" x2="314" y2="314"/>\n'
'    <line x1="314" y1="198" x2="198" y2="314"/>\n'
'    <circle cx="256" cy="256" r="55" fill="none"/>\n'
'  </g>\n'
'  <path d="M 210 215 Q 230 185 270 195" stroke="white" stroke-width="2.5" fill="none" opacity="0.35" stroke-linecap="round"/>\n'
'  <circle cx="220" cy="210" r="4" fill="white" opacity="0.3"/>\n'
'  <circle cx="300" cy="230" r="2" fill="white" opacity="0.2"/>\n'
'  <circle cx="280" cy="310" r="1.5" fill="white" opacity="0.15"/>\n'
'  <circle cx="256" cy="256" r="95" fill="none" stroke="#C4B5FD" stroke-width="1.5" opacity="0.3"/>\n'
'</svg>\n'
)

MONO = COLOR.replace('#1E1B4B', '#111827')
MONO = MONO.replace('#C4B5FD', '#D1D5DB')
MONO = MONO.replace('#7C3AED', '#9CA3AF')
MONO = MONO.replace('#5B21B6', '#6B7280')
MONO = MONO.replace('#F59E0B', '#E5E7EB')
MONO = MONO.replace('#2E2860', '#1F2937')

with open('avatars/claude-avatar.svg', 'w') as f:
    f.write(COLOR)
with open('avatars/claude-avatar-mono.svg', 'w') as f:
    f.write(MONO)

print(f"Color: {len(COLOR)} bytes")
print(f"Mono:  {len(MONO)} bytes")
