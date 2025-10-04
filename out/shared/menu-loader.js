/**
 * DR ANMYTAS - Menu Loader Script
 * Tự động load menu component cho tất cả các trang
 */

// Menu HTML Template
const MENU_TEMPLATE = `
<div class="header-bottom wide-nav flex-has-center hide-for-medium" id="wide-nav">
  <div class="flex-row container">
    <div class="flex-col hide-for-medium flex-center">
      <ul class="nav header-nav header-bottom-nav nav-center nav-size-xlarge nav-spacing-xlarge nav-uppercase">
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-2068 menu-item-design-default" id="menu-item-2068">
          <a class="nav-top-link" href="/index.html">Homepage</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2067 menu-item-design-default" id="menu-item-2067">
          <a class="nav-top-link" href="/gioi-thieu/index.html">About Us</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2065 menu-item-design-default" id="menu-item-2065">
          <a class="nav-top-link" href="/shop/index.html">Products</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2099 menu-item-design-default" id="menu-item-2099">
          <a class="nav-top-link" href="/dao-tao/index.html">Training</a>
        </li>
        <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-2070 menu-item-design-default has-dropdown" id="menu-item-2070">
          <a aria-expanded="false" aria-haspopup="menu" class="nav-top-link" href="/tin-tuc/index.html">News<i aria-hidden="true" class="icon-angle-down"></i></a>
          <ul class="sub-menu nav-dropdown nav-dropdown-simple">
            <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2069" id="menu-item-2069">
              <a href="/bi-quyet-lam-dep/index.html">Beauty Tips</a>
            </li>
          </ul>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2838 menu-item-design-default" id="menu-item-2838">
          <a class="nav-top-link" href="/canh-bao-mua-hang/index.html">Purchase Warning</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2066 menu-item-design-default" id="menu-item-2066">
          <a class="nav-top-link" href="/lien-he/index.html">Contact</a>
        </li>
        <li class="header-search header-search-lightbox has-icon">
          <div class="header-button"> 
            <a aria-controls="search-lightbox" aria-expanded="false" aria-haspopup="dialog" aria-label="Search" class="icon primary button round is-small" data-flatsome-role-button="" data-focus="input.search-field" data-open="#search-lightbox" href="#search-lightbox" role="button">
              <i aria-hidden="true" class="icon-search" style="font-size:16px;"></i>
            </a> 
          </div>
          <div class="mfp-hide dark text-center" id="search-lightbox">
            <div class="searchform-wrapper ux-search-box relative form-flat is-large">
              <form action="/index.html" class="searchform" method="get" role="search">
                <div class="flex-row relative">
                  <div class="flex-col flex-grow">
                    <label class="screen-reader-text" for="woocommerce-product-search-field-0">Search for:</label>
                    <input class="search-field mb-0" id="woocommerce-product-search-field-0" name="s" placeholder="Search…" type="search" value=""/>
                    <input name="post_type" type="hidden" value="product"/>
                  </div>
                  <div class="flex-col">
                    <button aria-label="Submit" class="ux-search-submit submit-button secondary button icon mb-0" type="submit" value="Search">
                      <i aria-hidden="true" class="icon-search"></i> 
                    </button>
                  </div>
                </div>
                <div class="live-search-results text-left z-top"></div>
              </form>
            </div> 
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>
`;

/**
 * Load menu component into target element
 */
function loadDRAnmytasMenu(targetSelector = '#wide-nav') {
  const target = document.querySelector(targetSelector);
  if (target) {
    target.outerHTML = MENU_TEMPLATE;
    setActiveMenuItem();
    console.log('✅ DR ANMYTAS Menu loaded successfully');
  } else {
    console.warn('⚠️ Menu target element not found:', targetSelector);
  }
}

/**
 * Set active menu item based on current page
 */
function setActiveMenuItem() {
  const currentPath = window.location.pathname;
  const menuItems = document.querySelectorAll('.nav-top-link');
  
  // Remove active classes from all items
  document.querySelectorAll('.menu-item').forEach(item => {
    item.classList.remove('current-menu-item', 'current_page_item', 'current', 'active');
  });
  
  // Add active class to current page
  menuItems.forEach(link => {
    const href = link.getAttribute('href');
    if (href) {
      const cleanHref = href.replace('/index.html', '/').replace('index.html', '');
      const cleanPath = currentPath.replace('index.html', '');
      
      if (cleanPath === cleanHref || 
          (cleanPath === '/' && href.includes('index.html')) ||
          (cleanPath.includes(cleanHref) && cleanHref !== '/')) {
        const menuItem = link.closest('.menu-item');
        if (menuItem) {
          menuItem.classList.add('current-menu-item', 'current_page_item', 'current', 'active');
        }
      }
    }
  });
}

/**
 * Replace existing menu with shared menu
 */
function replaceDRAnmytasMenu() {
  // Find existing menu
  const existingMenu = document.querySelector('#wide-nav') || 
                      document.querySelector('.header-bottom-nav').closest('.header-bottom');
  
  if (existingMenu) {
    const container = existingMenu.parentElement;
    existingMenu.remove();
    container.insertAdjacentHTML('beforeend', MENU_TEMPLATE);
    setActiveMenuItem();
    console.log('✅ DR ANMYTAS Menu replaced successfully');
  }
}

// Auto-initialize when DOM is loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', replaceDRAnmytasMenu);
} else {
  replaceDRAnmytasMenu();
}

// Export for manual usage
window.DRAnmytasMenu = {
  load: loadDRAnmytasMenu,
  replace: replaceDRAnmytasMenu,
  setActive: setActiveMenuItem
};