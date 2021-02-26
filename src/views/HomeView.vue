<template>
  <div class="wrapper">
    <h1 class="main-title">Список психотерапевтов</h1>
    <div
      class="psychotherapist-list_empty"
      v-if="psychotherapistsArr.length === 1"
      key="psychotherapist-list"
    >
      <span>В списке нет психотерапевтов</span>
    </div>
    <div
      class="psychotherapist-list"
      v-else
      key="psychotherapist-list"
    >
      <div
        class="psychotherapist-list__psychotherapist"
        v-for="(psychotherapist, index) in psychotherapistsArr"
        :key="index"
      >
        <router-link
          class="psychotherapist-list__psychotherapist-link"
          :to="{
            name: 'PsychotherapistInfoView',
            params: {
              id: (psychotherapist.id).toString(),
              psychotherapist: psychotherapist
            }
          }"
        >
          <img
            class="psychotherapist-list__psychotherapist-photo"
            :src="psychotherapist.photo_url_small"
            alt=""
          />
          <span
            class="psychotherapist-list__psychotherapist-name"
          >
            {{ psychotherapist.name }}
          </span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data () {
    return {
      psychotherapistsArr: {},
    }
  },
  methods: {
    loadContactArr () {
      this.$_fetch(
        '/read',
        {}
      ).then(
        response => response.json()
      ).then(
        response => this.psychotherapistsArr = response
      )
    },
  },
  created () {
    this.loadContactArr()
  },
}
</script>

<style lang="sass" scoped>
.psychotherapist-list, .psychotherapist-list_empty
  display: flex
  flex: 0 1 auto
  flex-flow: column nowrap

.psychotherapist-list
  padding-bottom: 0.5rem

  &__psychotherapist
    display: flex
    flex: 0 1 auto
    flex-flow: row nowrap
    justify-content: space-between

    padding: 0.5rem
    box-shadow: 1px 1px 3px lightgrey

  &__psychotherapist-link
    display: grid
    grid-template-columns: 2fr 8fr
    width: 100%

    color: black
    text-decoration: none

  &__psychotherapist-photo
    grid-column: 1

  &__psychotherapist-name
    grid-column: 2
</style>
