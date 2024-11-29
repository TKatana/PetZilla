<?php
// Include your database connection
include 'db_connection.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Check if a file was uploaded
    if (isset($_FILES['product_img']) && $_FILES['product_img']['error'] === UPLOAD_ERR_OK) {
        // ImageBB API Key
        $api_key = '0e6baf4be28d199e0460815cab4b007a';

        // Get the image data
        $product_img = $_FILES['product_img']['tmp_name'];
        $image_data = file_get_contents($product_img);
        $base64_image = base64_encode($image_data);

        // Prepare the payload for ImageBB
        $data = [
            'key' => $api_key,
            'image' => $base64_image,
        ];

        // cURL to send the image to ImageBB
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://api.imgbb.com/1/upload');
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($ch);
        curl_close($ch);

        // Decode the response
        $response_data = json_decode($response, true);

        // Check if the upload was successful
        if (isset($response_data['data']['url'])) {
            $image_url = $response_data['data']['url'];

            // Store the URL in the database
            $stmt = $conn->prepare("INSERT INTO product_img (url) VALUES (?)");
            $stmt->bind_param("s", $image_url);

            if ($stmt->execute()) {
                echo "Image uploaded successfully! URL saved in database: <a href='$image_url' target='_blank'>$image_url</a>";
            } else {
                echo "Failed to save image URL in database.";
            }

            $stmt->close();
        } else {
            echo "Image upload failed. Error: " . $response_data['error']['message'];
        }
    } else {
        echo "No image file selected or there was an error uploading the file.";
    }
}

// Close the database connection
$conn->close();
?>
