<?php
// Add custom Theme Functions here

// Function gallery
function thongtingallery(){
	ob_start();
	?>
		<div class="card-body"><div class="st-pd-table"><?php the_field('thongtin-gallery')?></div></div>
	<?php
	$result = ob_get_contents();
	ob_end_clean();
	return $result;
}
add_shortcode('thongtin-gallery', 'thongtingallery');


// Function thông tin chi tiết
function thongtinchitiet(){
	ob_start();
	?>
		<div class="card-body"><div class="st-pd-table"><?php the_field('thongtin-sanpham')?></div></div>
	<?php
	$result = ob_get_contents();
	ob_end_clean();
	return $result;
}
add_shortcode('thongtin-sanpham', 'thongtinchitiet');

// Function thông tin video
function thongtinvideo(){
	ob_start();
	?>
		<div class="card-body"><div class="st-pd-table"><?php the_field('thongtin-video')?></div></div>
	<?php
	$result = ob_get_contents();
	ob_end_clean();
	return $result;
}
add_shortcode('thongtin-video', 'thongtinvideo');

// Function thông tin description
function add_thongtin_and_link_after_product_title() {
	global $product;

	if ( ! $product ) return;

	$product_id = $product->get_id();
	$link = get_permalink( $product_id );
	$thongtin = get_field('thongtin-description', $product_id);

	echo '<div class="cus-thongtinthem">';

	// Nếu có nội dung thì hiển thị mô tả
	if ( $thongtin ) {
		echo '<div class="card-body"><div class="st-pd-table">' . wp_kses_post( $thongtin ) . '</div></div>';
	}

	// Nút "Xem chi tiết" luôn hiển thị
	echo '<div class="view-details-link">';
		echo '<a href="' . esc_url( $link ) . '">Xem chi tiết <i class="fa-solid fa-angle-right"></i></a>';
	echo '</div>';

	echo '</div>';
}
add_action( 'woocommerce_shop_loop_item_title', 'add_thongtin_and_link_after_product_title', 11 );





/** Dich tieng viet */
function ra_change_translate_text( $translated_text ) {
if ( $translated_text == 'Old Text' ) {
$translated_text = 'New Translation';
}
return $translated_text;
}
add_filter( 'gettext', 'ra_change_translate_text', 20 );
function ra_change_translate_text_multiple( $translated ) {
$text = array(
'Mô tả' => 'Thông tin sản phẩm',
'Shop' => 'DR.ANMYTAS',
'Quick View' => 'Xem nhanh',
'Oops! That page can’t be found' => 'Lỗi 404! Trang web không tồn tại',
'It looks like nothing was found at this location. Maybe try one of the links below or a search'=> 'Chúng tôi không tìm thấy trang này trên hệ thống, vui lòng thử chức năng tìm kiếm bên dưới',
'Leave a comment' => 'Viết bình luận',
'Continue reading' => 'Đọc tiếp',
'View more' => 'Xem thêm',
'Category Archives' => 'Danh mục',
'Posted in' => 'Đăng tại',
'POSTED ON' => 'Đăng ngày',
'SHOPPING CART' => 'Giỏ hàng',
'CHECKOUT DETAILS' => 'Thông tin thanh toán',
'ORDER COMPLETE' => 'Hoàn tất đặt hàng',
'CATEGORY ARCHIVES' => 'Chuyên mục',
'MY ACCOUNT'=> 'Tài khoản của tôi',
'Sản phẩm tương tự'=>'KHÁM PHÁ THÊM',
);
$translated = str_ireplace( array_keys($text), $text, $translated );
return $translated;
}
add_filter( 'gettext', 'ra_change_translate_text_multiple', 20 );

function custom_sku_brand_shortcode($atts) {
    if (!is_product()) {
        return ''; // Chỉ hiển thị trên trang sản phẩm
    }
    
    global $product;
    
    if (!$product) {
        return '';
    }
    
    // Lấy SKU
    $sku = $product->get_sku();
    
    // Lấy thương hiệu (brand) - Giả sử thương hiệu lưu dưới taxonomy 'product_brand'
    $brands = wp_get_post_terms($product->get_id(), 'product_brand');
    $brand_name = !empty($brands) ? esc_html($brands[0]->name) : 'N/A';
    
    // Hiển thị thông tin SKU và Brand
    return '<p><strong>SKU:</strong> ' . esc_html($sku) . '</p>' .
           '<p><strong>Brand:</strong> ' . esc_html($brand_name) . '</p>';
}
add_shortcode('sku_brand', 'custom_sku_brand_shortcode');


function block_all_video_fullscreen() {
    ?>
    <style>
      video::-webkit-media-controls-fullscreen-button {
        display: none !important;
      }
      video::-webkit-media-controls {
        overflow: hidden !important;
      }
    </style>
    <script>
      document.addEventListener('DOMContentLoaded', function () {
        const video = document.getElementById('myVideo');

        if (video) {
          video.removeAttribute('controls');
          video.setAttribute('playsinline', '');
          video.setAttribute('muted', '');
        }

        if (video.requestFullscreen) {
          video.requestFullscreen = function () { console.log('Blocked fullscreen'); };
        }
        if (video.webkitEnterFullscreen) {
          video.webkitEnterFullscreen = function () { console.log('Blocked iOS fullscreen'); };
        }
        if (video.mozRequestFullScreen) {
          video.mozRequestFullScreen = function () { console.log('Blocked Firefox fullscreen'); };
        }

        document.addEventListener('keydown', function (e) {
          if (e.key.toLowerCase() === 'f' || e.key === 'F11') {
            e.preventDefault();
            console.log("Prevented fullscreen key");
          }
        });

        document.addEventListener('fullscreenchange', function () {
          if (document.fullscreenElement) {
            document.exitFullscreen();
            console.log("Force exit fullscreen");
          }
        });
      });
    </script>
    <?php
}
add_action('wp_footer', 'block_all_video_fullscreen');


function suacss_preview() {
    if (is_customize_preview()) {
        wp_add_inline_style('customize-controls', '
            #customize-outer-theme-controls .accordion-section-title,
            #customize-theme-controls .accordion-section-title {
                color: #50575e;
                background-color: #fff;
                border-bottom: 1px solid #dcdcde;
                border-left: 4px solid #fff;
                transition: .15s color ease-in-out, .15s background-color ease-in-out, .15s border-color ease-in-out;
                display: flex;
                align-items: center;
            }
        ');
    }
}

add_action('admin_enqueue_scripts', 'suacss_preview');

//* Remove non-breaking space from beginning of paragraph
add_filter( 'the_excerpt', function( $excerpt ) {
  return str_replace( [ '<p>&nbsp; ', '<p>&nbsp;' ], '<p>', $excerpt );
}, 999, 1 );
