import { Component, OnInit, Input } from "@angular/core";
import { User, Match } from "src/app/_models";
import { RouletteRequestType } from "src/app/_services";

@Component({
  selector: "misc-user-card",
  templateUrl: "./user-card.component.html",
  styleUrls: ["./user-card.component.scss"],
})
export class UserCardComponent implements OnInit {
  @Input() readonly user: User;
  @Input() readonly type: RouletteRequestType;
  @Input() readonly match: Match;

  img: string;

  constructor() {}
  ngOnInit(): void {
    this.img =
      this.type === "tutor" &&
      !(this.user.tutordata.profilePicture as string).includes("undefined")
        ? this.user.tutordata.profilePicture
        : "assets/img/icons/user_default.png";
  }

  get tutordata() {
    return this.match.tutor.tutordata;
  }
  get schoolData() {
    return this.match.student.studentdata.schoolData;
  }
}
