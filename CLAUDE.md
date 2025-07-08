# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a web-based prototype system for TOYO TIRES application, containing multiple design iterations and HTML prototypes. The project consists of static HTML files with embedded CSS and JavaScript, organized into design versions with comprehensive mobile-responsive interfaces.

## Architecture

### Directory Structure
- **Root level**: `index.html` - Main design gallery showcasing all design iterations
- `design-0/` - Consolidated prototype collections:
  - `all-15-b2b-prototypes.html`, `all-15-b2c-prototypes.html` - Complete prototype viewers
  - `bonus-b2b-prototypes.html`, `bonus-b2c-prototypes.html` - Additional prototype collections
- `design-1/`, `design-2/`, `design-3/` - Different design iterations, each containing:
  - `combined-index.html` - Main prototype showcase file displaying all screens
  - Individual HTML files for specific screens (home, campaigns, warranty, etc.)
  - `index.html` - Navigation/landing page for each design iteration
- `images/` - Shared image assets (logos, campaigns, UI elements)

### Key Files
- `convert_images_to_base64.py` - Python utility to embed images as base64 data URIs in HTML files for better compatibility with design tools. Do not run this file.

### Technical Stack
- Pure HTML/CSS/JavaScript (no build system)
- TailwindCSS via CDN
- Font Awesome icons via CDN
- Responsive design using CSS Grid and Flexbox

## Development Commands

### Image Processing
```bash
python3 convert_images_to_base64.py
```
Converts image references to base64 data URIs in HTML files. Run this when:
- Adding new images to the `images/` directory
- Preparing files for design tool import
- Ensuring cross-platform compatibility


### File Serving
Since these are static HTML files, serve them using:
```bash
python3 -m http.server 8000
```
Then navigate to:
- `http://localhost:8000/` - Main design gallery (root index.html)
- `http://localhost:8000/design-0/` - For consolidated prototype collections
- `http://localhost:8000/design-X/` - For individual design iterations (where X = 1, 2, or 3)

## Prototype Development Workflow

### Standard Design Brief

**Context**: We are building a prototype for a company called "TOYO TIRES". When creating new high-fidelity prototype screens, follow the instructions below to complete prototype designs ensuring that these prototype screens can be directly used for development:

### High-Fidelity Prototype Design Process

1. **User Experience Analysis**: First, analyze the main functions and user needs of this app to determine the core interaction logic.
2. **Product Interface Planning**: As a product manager, define key interfaces to ensure a reasonable information architecture.
3. **High-Fidelity UI Design**: As a UI designer, create interfaces that closely follow the real iOS design guidelines, using modern UI elements to provide the best visual experience. The primary theme color is #2563EB.
4. **HTML Prototype Implementation**: Use **HTML + Tailwind CSS** to generate all prototype screens, and use **FontAwesome** (or other open-source UI components) to enhance the design, making it more refined and closer to a real app.

### Interface Structure and Display Requirements

#### Modular Interface Files
Each interface should be stored as a separate HTML file, clearly named (e.g., home-feature-1.html, home-feature-2.html, home-feature-3.html, etc.).

#### Main Entry Point (index.html)
The index.html file will act as the main container. Do not include actual interface HTML code directly in this file. Instead, embed all interface files using <iframe> elements.

All interfaces should be visible together on the page (stacked or laid out side-by-side) — do not use navigation links to toggle views.

The main container (index.html) must be minimal, with no padding, margin, or spacing applied to the <body>, <html>, or <iframe> elements. This ensures that each embedded interface is rendered in its true dimensions and styling without interference.

#### Visual Realism and Mobile Simulation

Each iframe content (individual HTML files) should simulate an iPhone 16 Pro:
- Match the exact dimensions and aspect ratio of the device
- Use rounded corners and wrap each screen in a flat device mockup frame
- Include a top iOS-style status bar (e.g., time, signal, battery indicators)
- Add a bottom app navigation tab bar styled similarly to native iOS tab bars
- If an interface is longer than one screen, do not use scrollviews — instead, increase the screen height to display all content fully in a single view

#### Asset Requirements
- The logo is `images/toyo-tires.png`
- Follow these requirements to generate complete HTML code, ensuring that it can be directly used for actual development

## Working with Prototypes

### Current Design Iterations
- **Design 0**: Consolidated prototype collections and overview files
- **Design 1**: Original TOYO TIRES CARE interface
- **Design 2**: Refined B2B/B2C variants 
- **Design 3**: Latest iteration with "boost" and "glass" UI variants, dark mode support

### Common Screens Across Designs
- Home/Dashboard
- Campaign management
- Warranty registration/claims
- Service centre finder
- Support/Help
- Order management (B2B)
- Sales forecasting (B2B)

## File Conventions

### HTML Structure

#### Prototype File Standards
- **Self-contained**: Each prototype file includes embedded CSS/JS
- **Mobile-first**: Responsive design prioritizing mobile experience
- **iOS Guidelines**: Follow Apple's Human Interface Guidelines
- **Navigation**: Consistent patterns across screens
- **Components**: Header/footer components embedded in each file

#### Development-Ready Output
- **Direct Implementation**: Prototypes should be ready for actual development
- **Clean Code**: Well-structured HTML with proper semantics
- **Accessibility**: Follow WCAG guidelines for accessibility
- **Performance**: Optimized for fast loading and smooth interactions

### Image Handling
- All images should be placed in the `images/` directory
- Reference images using relative paths: `../images/filename.ext`
- Do not run `convert_images_to_base64.py` to embed images for design tool compatibility, i'll do it manually
- Supported formats: PNG, JPG, JPEG, GIF, SVG, WebP

### Design System

#### Brand Colors
- **Primary Theme Color**: #2563EB (Blue)
- **Secondary**: #3B82F6 (Light Blue)
- **Gradient**: Blue gradient (#2563EB to #3B82F6)

#### Typography
- **System Fonts**: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto
- **iOS Style**: Follow Apple's Human Interface Guidelines for text hierarchy

#### UI Components
- **Cards**: Consistent border-radius: 20px
- **Shadows**: `0 10px 30px rgba(0,0,0,0.1)`
- **Icons**: FontAwesome for enhanced design refinement

#### iPhone 16 Pro Specifications
- **Screen Dimensions**: 393px × 852px (standard viewport)
- **Device Frame**: Rounded corners with flat mockup design
- **Status Bar**: iOS-style with time, signal, battery indicators
- **Tab Bar**: Bottom navigation following iOS tab bar patterns
- **Safe Areas**: Consider iPhone notch and bottom safe areas

#### Asset References
- **Logo**: `images/toyo-tires.png` (primary brand logo)
- **Image Path**: Use relative paths `../images/filename.ext`

## Deployment

### GitHub Pages (Primary Deployment Method)
This project uses GitHub Pages for deployment:
- **Automatic deployment** from the main branch
- **URL**: `https://pewepw.github.io/toyo_design/`
- **Process**: Push to main branch → GitHub Pages auto-deploys

### Deployment Structure
The current file structure is optimized for GitHub Pages:
- Root `index.html` serves as the main entry point
- All design iterations are self-contained in their directories
- Images are centralized in the `images/` directory
- No build process required - deploy directly from repository

## Git Workflow

### Branch Strategy
- Main development on feature branches
- Combined index files are primary deliverables
- Individual screen files support detailed development

### File Management
- Each design iteration maintains its own `index.html` and `combined-index.html`
- Copy variations (e.g., `campaign copy.html`) are used for iterative development
- Use descriptive commit messages for design changes
