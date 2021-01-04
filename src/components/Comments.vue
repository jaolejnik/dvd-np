<template>
    <div class="hello">
        <h2>Basic component exmaple.</h2>
        <p>
            The data below is added/removed from the PostgreSQL Database using Django's
            ORM and Rest Framework.
        </p>
        <br />
        <p><strong>Username</strong></p>
        <input type="text" placeholder="Enter your username" v-model="username" />
        <p><strong>Message</strong></p>
        <input type="text" placeholder="Enter your message" v-model="message" />
        <br /><br />
        <input
            type="submit"
            value="Add comment"
            @click="addComment({ username: username, message: message })"
            :disabled="!username || !message"
        />
        <hr />
        <br />
        <h3>Comments</h3>
        <p v-if="comments.length === 0">No comments</p>
        <div class="comment" v-for="(comment, index) in comments" :key="index">
            <p class="comment-index">[{{ index }}]</p>
            <p class="comment-subject">
                <strong>{{ comment.username }}</strong>
            </p>
            <p class="comment-body" v-html="comment.message"></p>
            <input type="submit" @click="deleteComment(comment.id)" value="Delete" />
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
    name: "Comments",

    data() {
        return {
            username: "",
            message: "",
        };
    },

    computed: mapState({
        comments: (state) => state.comments.comments,
    }),

    methods: mapActions("comments", ["addComment", "deleteComment"]),

    created() {
        this.$store.dispatch("comments/getComments");
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
    max-width: 65%;
}

.comment {
    margin: 0 auto;
    max-width: 30%;
    text-align: left;
    border-bottom: 1px solid #ccc;
    padding: 1rem;
}

.comment-index {
    color: #ccc;
    font-size: 0.8rem;
}

img {
    width: 250px;
    padding-top: 50px;
    padding-bottom: 50px;
}
</style>
