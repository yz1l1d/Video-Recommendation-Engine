# Video Recommendation Engine

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#video-recommendation-engine)

A sophisticated recommendation system that suggests personalized video content based on user preferences and engagement patterns using deep neural networks. Ref: to see what kind of motivational content you have to recommend, take reference from our Empowerverse App [ANDROID](https://play.google.com/store/apps/details?id=com.empowerverse.app) || [iOS](https://apps.apple.com/us/app/empowerverse/id6449552284).

## 🎯 Project Overview

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-project-overview)

This project implements a video recommendation algorithm that:

* Delivers personalized content recommendations
* Handles cold start problems using mood-based recommendations
* Utilizes deep neural networks for content analysis
* Integrates with external APIs for data collection
* Implements efficient data caching and pagination

## 🛠️ Technology Stack

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#%EF%B8%8F-technology-stack)

* **Backend Framework** : FastAPI
* **Documentation** : Swagger/OpenAPI

## 📋 Prerequisites

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-prerequisites)

* Virtual environment (recommended)

## 🚀 Getting Started

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-getting-started)

1. **Clone the Repository**
   ```shell
   git clone <repository-url>
   cd video-recommendation-engine
   ```
2. **Set Up Virtual Environment**
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```shell
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables** Create a `.env` file in the root directory:
   ```dotenv
   FLIC_TOKEN=your_flic_token
   API_BASE_URL=https://api.socialverseapp.com
   ```
5. **Run Database Migrations**
   ```shell
   alembic upgrade head
   ```
6. **Start the Server**
   ```shell
   uvicorn app.main:app --reload
   ```

## 📊 API Endpoints

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-api-endpoints)

### Main Recommendation Endpoints

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#main-recommendation-endpoints)

1. **Get Personalized Feed**

   ```
   GET /feed?username={username}
   ```

   Returns personalized video recommendations for a specific user.
2. **Get Category-based Feed**

   ```
   GET /feed?username={username}&category_id={category_id}
   ```

   Returns category-specific video recommendations for a user.

### Data Collection Endpoints (Internal Use)

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#data-collection-endpoints-internal-use)

The system uses the following APIs for data collection:

### APIs

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#apis)

1. **Get All Viewed Posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```
2. **Get All Liked Posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/like?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```
3. **Get All Inspired posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/inspire?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```
4. **Get All Rated posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/rating?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```
5. **Get All Posts** (Header required*) (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000
   ```
6. **Get All Users** (Header required*) (METHOD: GET):
   ```
   https://api.socialverseapp.com/users/get_all?page=1&page_size=1000
   ```

### Authorization

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#authorization)

For autherization pass `Flic-Token` as header in the API request:

Header:

```json
"Flic-Token": "flic_11d3da28e403d182c36a3530453e290add87d0b4a40ee50f17611f180d47956f"
```

 **Note** : All external API calls require the Flic-Token header:

## 🧮 Algorithm Implementation

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-algorithm-implementation)

The recommendation engine uses a Deep Neural Network (DNN) architecture with the following components:

1. **Data Preprocessing**
   * Feature engineering
   * Data normalization
   * Missing value handling
   * Categorical encoding
2. **Model Architecture**
   * Embedding layers for categorical features
   * Dense layers with ReLU activation
   * Dropout for regularization
   * Output layer with appropriate activation
3. **Cold Start Handling**
   * Mood-based initial recommendations
   * Content-based filtering fallback
   * Popularity-based recommendations

## 📝 Submission Requirements

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-submission-requirements)

1. **GitHub Repository**
   * Complete source code
   * This README.md file
   * Postman collection
   * Database migration scripts
2. **Video Submission**
   * Introduction Video (30-40 seconds)
     * Personal introduction
     * Project overview
   * Technical Demo
     * API demonstration using Postman
     * Database operations
     * Authentication flow
3. **Notification**
   * Join the Telegram group: [Video Recommendation](https://t.me/+VljbLT8o75QxN2I9)
   * Notify upon completion

## ✅ Evaluation Checklist

[](https://github.com/Tim-Alpha/video-recommendation-assignment?tab=readme-ov-file#-evaluation-checklist)

* [ ] All APIs are functional
* [ ] Database migrations work correctly
* [ ] README is complete and clear
* [ ] Postman collection is included
* [ ] Videos are submitted
* [ ] Code is well-documented
* [ ] Implementation handles edge cases
* [ ] Proper error handling is implemented
